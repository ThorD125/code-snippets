"use strict";

async function FETCTH(grepPoint, requestType, postBody) {
    const response = await fetch(`${grepPoint}`, {
        method: `${requestType}` || "GET",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(postBody) || "",
    });
    return await response.json();
}
