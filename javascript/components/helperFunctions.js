"use strict";

function exists(variableToCheck) {
    return typeof variableToCheck !== 'undefined';
}

function notExists(variableToCheck) {
    return !exists(variableToCheck);
}

function isEnter(key) {
    return key.keyCode === 13;
}

function isNull(givenval) {
    return givenval === null || givenval === "";
}

function notNull(givenval) {
    return !isNull(givenval);
}

function containsClass(targett, classe) {
    return targett.classList.contains(classe);
}

function notContainsClass(targett, classe) {
    return !containsClass(targett, classe);
}

function isZero(value) {
    return value === 0;
}

function notZero(value) {
    return !isZero(value);
}

function toPathParameter(value) {
    return value.replace(/\s/g, '_');
}
