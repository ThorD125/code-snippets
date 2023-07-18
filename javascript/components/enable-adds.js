document.body.innerHTML += '<div id="banner_ad" class="banner_ad">an add</div>'


function detector() {
    setTimeout(function () {

        if (!document.getElementsByClassName) return;
        var ads =
            document.getElementsByClassName('banner_ad'),
            ad = ads[ads.length - 1];

        if (!ad || ad.innerHTML.length == 0
            || ad.clientHeight === 0) {
            document.body.innerHTML += '<div id="myedad">Disable addblocker</div'
        } else {
            document.getElementById('banner_ad').style.display = 'none';
        }
    }, 2000);
}
document.addEventListener("DOMContentLoaded", detector, false);
