import React, { useState } from "react";
import { Link, useHistory } from "react-router-dom";

import "./Login.css";

export function Login({ onLogin }) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState(null);

    const history = useHistory();

    function handleLogin(event) {
        event.preventDefault();
        fetch("/login", {
            method: "POST",
            headers: { "Content-Type": "application/json"}, //, "Access-Control-Allow-Origin": "http://localhost:3000" },
            body: JSON.stringify({ username, password })
        }).then(res => res.json()).then(result => {
            if (result.result !== 200) {
                setError("Invalid login credentials");
            } else {
                onLogin(result.data["current_user"]);
                history.push("/profile");
            }
        });
    }
    
    return (
        <div id="login-block">
            <h2>Log In</h2>
            <hr />
            <form onSubmit={handleLogin}>
                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={e => {setError(null); setUsername(e.target.value);}}
                />

                <br />

                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={e => {setError(null); setPassword(e.target.value);}}
                />

                <br />

                {error && <div style={{color: "red"}}>{error}</div>}

                <br />

                <input type="submit" value="Log In" />
            </form>

            <p>Don't have an account? <Link to="/signup">Sign Up</Link></p>
        </div>
    );
}