const { defineConfig } = require('@vue/cli-service')
const NodePolyFillPlugin = require("node-polyfill-webpack-plugin")
module.exports = defineConfig({
  transpileDependencies: true,
  configureWebpack: {
    plugins: [
      new NodePolyFillPlugin()
    ]
  }
  
})
