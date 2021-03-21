// import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Switch, Route, NavLink } from "react-router-dom";
import { FaUserCircle } from "react-icons/fa";

import { CreateProfile } from "../CreateProfile/CreateProfile";
import { Home } from "../Home/Home";
import { Login } from "../Login/Login";
import { SignUp } from '../SignUp/SignUp';
import { Organizations } from "../Organizations/Organizations";
import { Events } from "../Events/Events";
import React, { useState } from 'react';

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
    const loggedIn = false;

    // const { token, setToken } = useToken();
    const token = null;
    const setToken = () => {};

    // if (!token) {
    //     return <Login setToken={setToken}></Login>
    // }

    return (
        <Router>
            <header>
                <NavLink to="/"><h1><span style={{color: "#c00"}}>NCSU</span> <span style={{color: "#000"}}>Involvement</span></h1></NavLink>

                <NavLink to="/orgs" activeClassName="active-link">Organizations</NavLink>
                <NavLink to="/events" activeClassName="active-link">Events</NavLink>
                {loggedIn ?
                    <div id="last-link">
                        <NavLink to="/profile" style={{marginRight: "5px"}}>Profile</NavLink>
                        <FaUserCircle size={25}/>
                    </div> :
                    <div id="last-link">
                        <NavLink to="/login">Log In</NavLink>
                    </div>
                }
                
            </header>
            <main>
                <Switch>
                    <Route exact path="/">
                        {/* <h1>Hello</h1> */}
                        <Home />
                    </Route>
                    <Route path="/orgs">
                        <Organizations />
                    </Route>
                    <Route path="/events">
                        <Events />
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
            </main>
        </Router>
    );
}
