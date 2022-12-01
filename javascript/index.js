"use strict";

import {
    exists,
    notExists,
    isEnter,
    isNull,
    notNull,
    containsClass,
    notContainsClass,
    isZero,
    notZero,
    toPathParameter
} from "./components/helperFunctions.js";

import {
    saveToLocalStorage,
    loadFromLocalStorage
} from "./components/local-storage.js";

import {
    FETCTH
} from "./components/fetching.js";

import {
    ALERT
} from "./components/alert.js";

document.addEventListener("DOMContentLoaded", init)

function init() {

    console.log("init");

}
