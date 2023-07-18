var time = 1;

var interval = setInterval(function() { 
   if (time <= 100) { 
            document.querySelector("#side-nav-following-see-all").click()
      time++;
   }
   else { 
      clearInterval(interval);
   }
    document.querySelector(".tiktok-j1fxk6-UlAccountList li:last-of-type").scrollIntoView({ behavior: "smooth" })
}, 1000);

list = ""
document.querySelectorAll(".tiktok-j1fxk6-UlAccountList li").forEach(function(x){list += x.querySelector("a").href + "," + x.querySelector("a").ariaLabel.replace("Profiel van ", "")+"\n"})

var element = document.createElement('a');
element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(list));
element.setAttribute('download', "toktiklijst.txt");

element.style.display = 'none';
document.body.appendChild(element);

element.click();

document.body.removeChild(element);
