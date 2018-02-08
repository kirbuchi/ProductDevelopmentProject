'use strict'

const process = require('process');
const API_BASE_URL = (process.env.API_BASE_URL || 'http://127.0.0.1:5000').replace(/\/+$/, '');

module.exports = {
  NODE_ENV: '"production"',
  API_BASE_URL: '"' + API_BASE_URL + '"',
}
