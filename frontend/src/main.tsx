import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.tsx";
import "./index.css";
import { TourProvider } from "@reactour/tour";

const steps = [
  {
    selector: "#add-new",
    content: "Click here to add a new project!",
  },
];

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <TourProvider
      showPrevNextButtons={false}
      showDots={false}
      showBadge={false}
      steps={steps}
    >
      <App />
    </TourProvider>
  </React.StrictMode>
);
