"use strict";

function saveToLocalStorage(key, value) {
    if (localStorage) {
        return localStorage.setItem(key, JSON.stringify(value));
    } else {
        return "error in localstorage";
    }
}

function loadFromLocalStorage(key) {
    if (localStorage) {
        return JSON.parse(localStorage.getItem(key));
    } else {
        return "error in localstorage";
    }
}
