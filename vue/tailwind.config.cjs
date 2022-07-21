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
        danger: "#FFA6A6 !important",
        "warning-custom": "#F4DA56 !important",
        "warning-custom-text": "rgba(244,212,86,0.66) !important",
        ok: "rgba(173,219,115,0.66) !important",
        "ok-text": "#ADDB73 !important",
        "n/a": "rgba(103,195,208,0.66) !important",
        "n/a-text": "#67C3D0 !important",
      },
      boxShadow: {
        card: "0px 0px 3px 1px rgb(0 0 0 / 0.1)",
      },
    },
  },
};
