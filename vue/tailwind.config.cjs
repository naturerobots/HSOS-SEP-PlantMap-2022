module.exports = {
  content: ["./src/**/*.{vue,js,ts}"],
  plugins: [],
  theme: {
    extend: {
      colors: {
        light: "#F8FAF9" /* not the best solution for colors */,
        background: "#F5F7F2",
        primary: "#79b729",
        primary_hover: "#26561D",
        primary_disable: "#B6C1A7",
        secondary: "#9C9B9B",
        secondary_hover: "#7A8882",
        secondary_disable: "#B0BAB6",
      },
      boxShadow: {
        card: "0px 0px 3px 1px rgb(0 0 0 / 0.1)",
      },
    },
  },
};
