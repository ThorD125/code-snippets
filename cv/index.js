class Block extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: "open" });
  }

  connectedCallback() {
    const titlee = document.createElement("h3");
    titlee.innerText = this.getAttribute("title");
    this.shadowRoot.appendChild(titlee);

    const wrapper = document.createElement("span");
    let span = document.createElement("span");
    span.classList.add("before");
    span.innerHTML = "{";
    wrapper.appendChild(span);
    if (
      this.getAttribute("text") !== null &&
      this.getAttribute("text") !== undefined &&
      this.getAttribute("text") !== ""
    ) {
      console.log(this.getAttribute("text"));
      const textt = document.createElement("p");
      textt.innerText = `${this.getAttribute("text")}`;
      textt.style.paddingLeft = "2rem";
      wrapper.appendChild(textt);
    }
    span = document.createElement("span");
    span.innerHTML = "}";
    wrapper.appendChild(span);
    this.shadowRoot.appendChild(wrapper);

    document.querySelector("before").addEventListener("click");
  }
}

customElements.define("my-block", Block);
