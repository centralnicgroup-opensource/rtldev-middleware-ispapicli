const { src, dest, series } = require("gulp");
const xo = require("gulp-xo");
const stylelint = require("gulp-stylelint");
const htmlhint = require("gulp-htmlhint");
const jsonlint = require("gulp-jsonlint");
const prettier = require("gulp-prettier");

/*
validate css code
*/
function css() {
  return src("assets/css/*.css").pipe(
    stylelint({
      failAfterError: true,
      reportOutputDir: "reports/lint",
      reporters: [{ formatter: "verbose", console: true }],
      debug: true,
    })
  );
}

/*
validate html
*/
function html() {
  return src("*.html")
    .pipe(htmlhint()) // check errors
    .pipe(htmlhint.reporter()) //display errors
    .pipe(htmlhint.failAfterError()); // fail on error
}

/*
validate javascript with eslint, ignores assetes/plugins
*/
function jsLintXO() {
  return src(["assets/js/**/*.js"])
    .pipe(
      xo({
        globals: ["jQuery", "$", "document", "window", "Stickyfill"], // Stickyfill is a js library
      })
    )
    .pipe(xo.format()) // display errors
    .pipe(xo.failAfterError()); // fail on errors
}

/*
validate json files
*/
function jsonLint() {
  return src(["package.json", ".stylelintrc.json", ".xo-config.json"])
    .pipe(jsonlint())
    .pipe(jsonlint.failOnError());
}

// can be triggered locally to format your code
exports.prettier = function () {
  return src([
    "assets/js/*.js",
    ".prettierrc.js",
    "gulpfile.js",
    "assets/css/*.css",
    "*.html",
    ".github/**/*.yml",
    "package.json",
  ])
    .pipe(prettier())
    .pipe(dest((file) => file.base));
};
// automatically triggered upon each push or pull request
exports.validate = series(jsonLint, jsLintXO, css, html);
