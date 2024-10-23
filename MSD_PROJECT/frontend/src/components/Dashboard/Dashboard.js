// Dashboard.js
import React from 'react';
import './Dashboard.css';

const Dashboard = () => {
    return (
        <div className="dashboard">
            <h2>Welcome to the Dashboard</h2>
            <p>Here is an overview of your activity.</p>
            <div className="dashboard-widgets">
                {/* 可以添加仪表板上的小部件 */}
                <div className="widget">Widget 1</div>
                <div className="widget">Widget 2</div>
                <div className="widget">Widget 3</div>
            </div>
        </div>
    );
};

export default Dashboard;
