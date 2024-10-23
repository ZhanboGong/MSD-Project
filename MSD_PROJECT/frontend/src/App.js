// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import LoginPage from './components/LoginPage/LoginPage';
import Dashboard from './components/Dashboard/Dashboard';
import SearchBar from './components/SearchBar/SearchBar';
import './App.css';  // 如果需要全局样式

function App() {
    return (
        <Router>
            <div className="App">
                <Switch>
                    {/* 默认路由，渲染登录页面 */}
                    <Route exact path="/" component={LoginPage} />

                    {/* 仪表板路由 */}
                    <Route path="/dashboard" component={Dashboard} />

                    {/* 搜索页面 */}
                    <Route path="/search" component={SearchBar} />

                    {/* 其他路由可以添加到这里 */}
                </Switch>
            </div>
        </Router>
    );
}

export default App;
