import { useState } from "react";
import { Link, useHistory } from "react-router-dom";

import "../Login/Login.css";

export function SignUp(props) {
    const history = useHistory();

    function handleSignUp(event) {
        event.preventDefault();
        if (password !== password2) {
            setError("Passwords must match");
        } else {
            fetch("/register", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username, password })
            }).then(res => res.json()).then(result => {
                if (result.result !== 200) {
                    setError("An account with this username already exists");
                } else {
                    history.push("/login");
                }
            });
        }
    }

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [password2, setPassword2] = useState("");
    const [error, setError] = useState(false);

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
                    onChange={e => {setError(null); setPassword2(e.target.value);}}
                />

                {error && <div style={{color: "red"}}>{error}</div>}

                <input type="submit" value="Sign Up" />
            </form>

            <p>Already have an account? <Link to="/login">Log In</Link></p>
        </div>
    );
}