/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        // FinSight dark terminal palette
        navy:    "#0B1929",
        "navy-light": "#0c1118",
        "navy-surface": "#111820",
        cyan:    "#00d4ff",
        "cyan-dim": "#0099BB",
        "cyan-light": "#E6F6FA",
        purple:  "#7b61ff",
        "purple-dim": "#5B4FC4",
        "purple-light": "#EEEDFB",
        teal:    "#00e5a0",
        "teal-dim": "#0F7A5A",
        coral:   "#ff4d6a",
        amber:   "#ffb84d",
        border:  "#1e2a38",
        "border-2": "#2a3a4e",
        muted:   "#627a96",
        dim:     "#3a5070",
      },
      fontFamily: {
        display: ['"DM Serif Display"', "serif"],
        ui:      ["Syne", "sans-serif"],
        mono:    ['"DM Mono"', "monospace"],
      },
      animation: {
        pulse: "pulse 1.4s ease-in-out infinite",
        blink: "blink 1.2s ease-in-out infinite",
      },
      keyframes: {
        pulse: {
          "0%, 100%": { opacity: "1" },
          "50%":       { opacity: "0.4" },
        },
        blink: {
          "0%, 100%": { opacity: "1" },
          "50%":       { opacity: "0.25" },
        },
      },
    },
  },
  plugins: [],
};
