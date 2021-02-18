const { src, series, dest } = require("gulp");
const through2 = require("through2");
const MDLint = require("markdownlint");

// lint markdown files
function markDownLinter() {
  let errorFound = false;
  return src(
    ["**/*.md", "!HISTORY.md", "!node_modules/**/*.md", "!dist/**/*.md"],
    { read: false }
  )
    .pipe(
      through2.obj(function (file, enc, next) {
        MDLint(
          {
            files: [file.relative],
            handleRuleFailures: true,
            config: {
              "line-length": false,
            },
          },
          function callback(err, result) {
            const resultString = (result || "").toString();
            if (resultString) {
              console.error(resultString, err);
              errorFound = true;
              //throw new Error('Linting error, check errors above.')
            }
            next(err, file);
          }
        );
      })
    )
    .on("end", () => {
      if (errorFound) {
        process.exit(1);
      }
    });
}

exports.validate = series(markDownLinter);
