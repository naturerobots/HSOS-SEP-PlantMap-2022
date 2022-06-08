module.exports = {
  content: ["./src/**/*.{vue,js,ts}"],
  plugins: [], //require("daisyui")
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
    },
  },
  daisyui: {
    themes: [
      {
        light: {
          primary: "#79b729",
          "primary-focus": "#26561D",
          "primary-content": "#ffffff",
          secondary: "#9C9B9B",
          "secondary-focus": "#7A8882",
          "secondary-content": "#ffffff",
          //"accent": "#37cdbe",
          // "accent-focus": "#2aa79b",
          // "accent-content": "#ffffff",
          //"neutral": "#2a2e37",
          // "neutral-focus": "#16181d",
          // "neutral-content": "#ffffff",
          "base-100": "#F5F7F2",
          // "base-200": "#2a2e37",
          // "base-300": "#16181d",
          // "base-content": "#ebecf0",
          // "info": "#66c6ff",
          // "success": "#87d039",
          // "warning": "#e2d562",
          // "error": "#ff6f6f"
        },
        dark: {
          primary: "#79b729",
          "primary-focus": "#26561D",
          "primary-content": "#ffffff",
          secondary: "#9C9B9B",
          "secondary-focus": "#7A8882",
          "secondary-content": "#ffffff",
          //"accent": "#37cdbe",
          // "accent-focus": "#2aa79b",
          // "accent-content": "#ffffff",
          //"neutral": "#2a2e37",
          // "neutral-focus": "#16181d",
          // "neutral-content": "#ffffff",
          "base-100": "#232B27",
          // "base-200": "#2a2e37",
          // "base-300": "#16181d",
          // "base-content": "#ebecf0",
          // "info": "#66c6ff",
          // "success": "#87d039",
          // "warning": "#e2d562",
          // "error": "#ff6f6f"
        },
      },
    ],
  },
};
