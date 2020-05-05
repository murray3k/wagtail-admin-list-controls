import React from "react";
import { render_control } from "./render_control";

export function Panel({control}) {
    return (
        <div className="alc__panel" style={control.style}>
            {control.children && control.children.map(control => render_control(control))}
        </div>
    );
}
