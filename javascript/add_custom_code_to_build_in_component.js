String.prototype.cleanup = function () {
    return this.toLowerCase().replace(/[^a-zA-Z0-9]+/g, "-");
}

console.log("stelkfjselfk;----///?.,".cleanup())
