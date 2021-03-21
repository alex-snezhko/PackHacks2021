import { useState } from "react";
import { Link } from "react-router-dom";

import "../Login/Login.css";

export function SignUp(props) {

    function handleSignUp(event) {
        if (password !== password2) {
            //
        }
    }

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [password2, setPassword2] = useState("");

    return (
        <div id="login-block">
            <h2>Sign Up</h2>
            <hr />
            <form onSubmit={handleSignUp}>
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

                <input
                    type="password"
                    placeholder="Confirm Password"
                    value={password2}
                    onChange={e => setPassword2(e.target.value)}
                />

                <input type="submit" value="Log In" />
            </form>

            <p>Already have an account? <Link to="/login">Log In</Link></p>
        </div>
    );
}