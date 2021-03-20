// import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Switch, Route, NavLink } from "react-router-dom";

import { CreateProfile } from "../CreateProfile/CreateProfile";
import { Home } from "../Home/Home";
import { Login } from "../Login/Login";
import { SignUp } from '../SignUp/SignUp';
import { useState } from 'react';

function useToken() {
    // const [token, setToken] = useState(JSON.parse(localStorage.getItem("token"))?.token);
    
    // return {
    //     token,
    //     setToken: userToken => {
    //         localStorage.setItem('token', JSON.stringify(userToken));
    //         setToken(userToken.token);
    //     },
    // };
}

export function App() {
    const loggedIn = true;

    // const { token, setToken } = useToken();
    const token = null;
    const setToken = () => {};

    // if (!token) {
    //     return <Login setToken={setToken}></Login>
    // }

    return (
        <Router>
            <header>
                <NavLink to="/"><h1>NCSU Get Involved</h1></NavLink>

                <NavLink to="/orgs" activeClassName="active-link">Organizations</NavLink>
                <NavLink to="/events" activeClassName="active-link">Events</NavLink>
                {loggedIn ?
                    <NavLink to="/profile">Profile</NavLink> :
                    <NavLink to="/login">Log In</NavLink>
                }
                
            </header>

            <Switch>
                <Route exact path="/">
                    {/* <h1>Hello</h1> */}
                    <Home />
                </Route>
                <Route path="/profile">
                    <CreateProfile />
                </Route>
                <Route path="/login">
                    <Login />
                </Route>
                <Route path="/signup">
                    <SignUp />
                </Route>
            </Switch>
        </Router>
    );
}
