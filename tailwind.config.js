/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./bytezo_website/templates/index.html"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("daisyui"),
  ],
}

