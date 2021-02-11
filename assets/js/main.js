$(document).ready(() => {
  /* ===== Stickyfill ===== */
  /* Ref: https://github.com/wilddeer/stickyfill */
  // Add browser support to position: sticky
  const elements = $(".sticky");
  Stickyfill.add(elements);

  /* Activate scrollspy menu */
  $("body").scrollspy({
    target: "#doc-menu",
    offset: 100,
  });

  /* Smooth scrolling */
  $("a.scrollto").on("click", function (event) {
    const target = this.hash;
    event.preventDefault();
    $("body").scrollTo(target, 800, {
      offset: 0,
      axis: "y",
    });
  });

  /* Bootstrap lightbox */
  /* Ref: http://ashleydw.github.io/lightbox/ */

  $(document).delegate('*[data-toggle="lightbox"]', "click", function (event) {
    event.preventDefault();
    $(this).ekkoLightbox();
  });
});
