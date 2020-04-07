const { override, fixBabelImports, adjustStyleLoaders } = require("customize-cra");

module.exports = override(
  // AntD Dynamic module import
  fixBabelImports("import", {
    libraryName: "antd",
    libraryDirectory: "es",
    style: "css",
  }),
  // Add Sass support
  adjustStyleLoaders(({ use: [, css, postcss, resolve, processor] }) => {
    // pre-processor
    if (processor && processor.loader.includes("sass-loader")) {
      processor.options.sourceMap = true; // sass-loader
    }
  })
);
