"use strict";

async function FETCTH(url, requestType, body) {
    const response = await fetch(`${url}`, {
        method: `${requestType}` || "GET",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(body) || "",
    });
    return await response.json();
}
