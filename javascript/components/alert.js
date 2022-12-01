"use strict";

document.addEventListener("DOMContentLoaded", initalert);

function initalert() {
    document.body.innerHTML += `<template id="alertTemplate">
    <div class="alert">
        <p>message</p>
        <i class="fa-solid fa-x fa-lg"></i>
    </div>
    </template>`;
}


function ALERT(message, type = "error") {
    // console.log(message);
    const $template = document.querySelector("template#alertTemplate").content.firstElementChild.cloneNode(true);
    const $board = document.querySelector("body");
    $board.insertAdjacentHTML("afterbegin", $template.outerHTML);
    document.querySelector(".alert").classList.add(type);
    document.querySelector(".alert p").innerText = message;
    document.querySelector(".alert i").addEventListener('click', closeAlert);
    setInterval(function () {
        try {
            document.querySelector(".alert i").click();
        } catch (e) {}
    }, 5000);
}

function closeAlert() {
    this.closest('.alert').remove();
    // console.log("clicked");
}
