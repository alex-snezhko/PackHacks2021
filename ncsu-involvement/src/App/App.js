// import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Switch, Route, NavLink, Redirect } from "react-router-dom";
import { FaUserCircle } from "react-icons/fa";

import { CreateProfile } from "../CreateProfile/CreateProfile";
import { Home } from "../Home/Home";
import { Login } from "../Login/Login";
import { SignUp } from '../SignUp/SignUp';
import { Organizations } from "../Organizations/Organizations";
import { Events } from "../Events/Events";
import React, { useState } from 'react';

// function useToken() {
//     // const [token, setToken] = useState(JSON.parse(localStorage.getItem("token"))?.token);
    
//     // return {
//     //     token,
//     //     setToken: userToken => {
//     //         localStorage.setItem('token', JSON.stringify(userToken));
//     //         setToken(userToken.token);
//     //     },
//     // };
// }

export function App() {
    // const loggedIn = false;
    const [userLoggedIn, setUserLoggedIn] = useState(null);

    // const { token, setToken } = useToken();
    // const token = null;
    // const setToken = () => {};

    // if (!token) {
    //     return <Login setToken={setToken}></Login>
    // }
    const loggedIn = userLoggedIn !== null;

    return (
        <Router>
            <header>
                <NavLink to="/"><h1><span style={{color: "#c00"}}>NCSU</span> <span style={{color: "#000"}}>Involvement</span></h1></NavLink>

                {loggedIn ? (
                    <React.Fragment>
                        <NavLink to="/orgs" activeClassName="active-link">Organizations</NavLink>
                        <NavLink to="/events" activeClassName="active-link">Events</NavLink>
                    
                        <div id="last-link">
                            <FaUserCircle size={25}/>
                            <NavLink to="/profile" style={{marginLeft: "5px"}}>Profile</NavLink>
                            <NavLink to="/login" style={{marginLeft: "30px"}} onClick={() => setUserLoggedIn(null)}>Log Out</NavLink>
                        </div>
                    </React.Fragment>
                    ) : (
                        <div id="last-link">
                            <NavLink to="/login">Log In</NavLink>
                        </div>
                    )
                }
                
            </header>
            <main>
                <Switch>
                    <Route exact path="/">
                        {!loggedIn ? <Redirect to="/login" /> : <Home userLoggedIn={userLoggedIn} />}
                    </Route>
                    <Route path="/orgs">
                        {!loggedIn ? <Redirect to="/login" /> : <Organizations />}
                    </Route>
                    <Route path="/events">
                        {!loggedIn ? <Redirect to="/login" /> : <Events />}
                    </Route>
                    <Route path="/profile">
                        {!loggedIn ? <Redirect to="/login" /> : <CreateProfile userLoggedIn={userLoggedIn} />}
                    </Route>
                    <Route path="/login">
                        <Login onLogin={setUserLoggedIn} />
                    </Route>
                    <Route path="/signup">
                        <SignUp />
                    </Route>
                </Switch>
            </main>
        </Router>
    );
}
