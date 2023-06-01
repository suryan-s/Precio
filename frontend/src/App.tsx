import { Router, Route } from "wouter";
import { useLocationProperty, navigate, BaseLocationHook } from "wouter/use-location";
import Login from "@/components/authentication/pages/Login";
import Signup from "@/components/authentication/pages/Signup";
import Home from "@/components/dashboard/pages/Home";
// returns the current hash location in a normalized form
// (excluding the leading '#' symbol)
const hashLocation = () => window.location.hash.replace(/^#/, "") || "/";

const hashNavigate = (to:string) => navigate("#" + to);

const useHashLocation:BaseLocationHook = () => {
  const location = useLocationProperty(hashLocation);
  return [location, hashNavigate];
};

const App = () => (
  <Router hook={useHashLocation}>
    <Route path="/" component={Home} />
    <Route path="/Login" component={Login} />
    <Route path="/Signup" component={Signup} />
  </Router>
);

export default App;