import React, { useState } from 'react';

function PatientRecordForm() {
    const [record, setRecord] = useState({ name: '', disease: '', procedure: '' });

    const handleSubmit = async (e) => {
        e.preventDefault();
        // 发送POST请求以新增记录
        const response = await fetch('/api/records', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(record),
        });
        const result = await response.json();
        alert(result.message);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Patient Name"
                value={record.name}
                onChange={(e) => setRecord({ ...record, name: e.target.value })}
            />
            <input
                type="text"
                placeholder="Disease"
                value={record.disease}
                onChange={(e) => setRecord({ ...record, disease: e.target.value })}
            />
            <input
                type="text"
                placeholder="Procedure"
                value={record.procedure}
                onChange={(e) => setRecord({ ...record, procedure: e.target.value })}
            />
            <button type="submit">Add Record</button>
        </form>
    );
}

export default PatientRecordForm;
