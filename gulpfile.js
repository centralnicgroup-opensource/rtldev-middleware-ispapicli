const { src, parallel } = require('gulp');
const gulp = require('gulp');
const xo = require('gulp-xo');
const csslint = require('gulp-csslint');
const htmlhint = require("gulp-htmlhint");
// import { htmlValidator } from 'gulp-w3c-html-validator';


/*
validate css code
*/
function css() {
  return gulp.src('/assets/css/*.css')
    .pipe(csslint())
    .pipe(csslint.formatter()); // display errors
  //.pipe(csslint.formatter('fail')); // fail on error 
}

/*
validate html
*/
function html() {
  return gulp.src("*.html")
    .pipe(htmlhint()) // check errors
    .pipe(htmlhint.reporter()); //display errors
  //.pipe(htmlhint.failAfterError()); // fail on error
}

/*
validate javascript with eslint, ignores assetes/plugins
*/
function eslintXO() {
  return src(['assets/js/**/*.js'])
    .pipe(xo({
      "globals": [
        "jQuery",
        "$",
        "document"
      ]
    }))
    .pipe(xo.format()); // display errors
  //.pipe(xo.failAfterError()); // fail on errors
}

exports.validate = parallel(css, html, eslintXO);
