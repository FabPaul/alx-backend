const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const app = express();
const port = 1245;

const client = redis.createClient();

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const listProducts = [
  { Id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { Id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { Id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { Id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

function getItemById(id) {
  return listProducts.find(product => product.Id === id);
}

async function reserveStockById(Id, stock) {
  await setAsync(`item.${Id}`, stock);
}

async function getCurrentReservedStockById(Id) {
  const reservedStock = await getAsync(`item.${Id}`);
  return reservedStock ? parseInt(reservedStock) : 0;
}

app.get('/list_products', (req, res) => {
  res.json(listProducts.map(product => ({
    Id: product.Id,
    name: product.name,
    price: product.price,
    stock: product.stock
  })));
});

app.get('/list_products/:itemId', async (req, res) => {
  const Id = parseInt(req.params.Id);
  const product = getItemById(Id);
  if (product) {
    const currentQuantity = await getCurrentReservedStockById(Id);
    res.json({ ...product, currentQuantity });
  } else {
    res.status(404).json({ status: 'Product not found' });
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const Id = parseInt(req.params.Id);
  const product = getItemById(Id);
  if (!product) {
    res.status(404).json({ status: 'Product not found' });
  } else {
    const currentQuantity = await getCurrentReservedStockById(Id);
    if (currentQuantity >= product.stock) {
      res.json({ status: 'Not enough stock available', Id });
    } else {
      await reserveStockById(Id, currentQuantity + 1);
      res.json({ status: 'Reservation confirmed', Id });
    }
  }
});

app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});
