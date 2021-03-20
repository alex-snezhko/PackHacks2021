import React, { useState } from "react";
import { Link } from "react-router-dom";

export function Login({ setToken }) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    function handleLogin(event) {
        event.preventDefault();
        fetch("/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password })
        }).then(res => res.json()).then(token => setToken(token));
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
                    onChange={e => setUsername(e.target.value)}
                />

                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={e => setPassword(e.target.value)}
                />

                <input type="submit" value="Log In" />
            </form>

            <p>Don't have an account? <Link to="/signup">Sign Up</Link></p>
        </div>
    );
}