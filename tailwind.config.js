/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./bytezo_website/templates/index.html",
    "./bytezo_website/templates/message.html"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("daisyui"),
  ],
}

