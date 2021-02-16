const { src, series, dest } = require("gulp");
const format = require("gulp-format-md");
const prettier = require("gulp-prettier");
const through2 = require("through2");
const markdownlint = require("markdownlint");

// use gulp-format-md 
function formatMD() {
    return src(["**/*.md", "!HISTORY.md"])
        .pipe(format())
        .pipe(dest('.')); // immediately format md files;
}

// use prettier to format
function formatWithPrettier() {
    return src(["**/*.md", "!HISTORY.md"])
        .pipe(prettier())
        .pipe(dest((file) => file.base));
}

// lint markdown files
function lintMarkDown() {
    return src(["**/*.md", "!HISTORY.md", "!node_modules/**/*.md"], { "read": false })
        .pipe(through2.obj(function obj(file, enc, next) {
            markdownlint(
                {
                    "files": [file.relative],
                    "handleRuleFailures": true,
                    "config": {
                        "line-length": false
                    }
                },
                function callback(err, result) {
                    const resultString = (result || "").toString();
                    if (resultString) {
                        console.log(resultString);
                        throw new Error('Linting error, check errors above.')
                    }
                    next(err, file);
                });
        }));
}

exports.validate = series(lintMarkDown);
