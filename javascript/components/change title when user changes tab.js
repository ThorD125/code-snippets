let doctitle = document.title;
window.addEventListener("focus", function () {
    document.title = doctitle;
});

window.addEventListener("blur", function () {
    document.title = "Come back!";
});
