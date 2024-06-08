import React, { useState } from 'react';

const sharedClasses = {
    input: 'form-radio h-5 w-5 text-blue-600 dark:text-blue-400',
    text: 'text-lg text-zinc-800 dark:text-zinc-200',
    button: 'bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-md',
    container: 'max-w-lg mx-auto p-4',
    textarea: 'w-full h-32 bg-zinc-100 dark:bg-zinc-800 text-lg p-2 rounded-md resize-none',
    label: 'flex items-center space-x-2 cursor-pointer'
};

const PhilosopherComponent = () => {
    const [text, setText] = useState('');
    const [selectedPhilosophy, setSelectedPhilosophy] = useState('Stoicism');

    const handleSend = async () => {
        const data = {
            "Query": text,
            "philosopher": selectedPhilosophy
        };

        try {
            const response = await fetch('http://backend:8080', {
                method: 'POST',
                body: JSON.stringify(data),
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            if (response.ok) {
                alert('Data sent successfully!');
            } else {
                alert('Failed to send data. Please try again.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        }
    };

    return (
        <div className={sharedClasses.container}>
            <h1 className="text-2xl font-bold text-center text-zinc-800 dark:text-zinc-200 mb-4">Philosopher</h1>
            <textarea
                className={sharedClasses.textarea}
                placeholder="Type your text here..."
                value={text}
                onChange={(e) => setText(e.target.value)}
            ></textarea>
            <div className="mt-4 flex items-center justify-between">
                <label className={sharedClasses.label}>
                    <input
                        type="radio"
                        name="philosophy"
                        className={sharedClasses.input}
                        checked={selectedPhilosophy === 'Stoicism'}
                        onChange={() => setSelectedPhilosophy('Stoicism')}
                    />
                    <span className={sharedClasses.text}>Stoicism</span>
                </label>
                <label className={sharedClasses.label}>
                    <input
                        type="radio"
                        name="philosophy"
                        className={sharedClasses.input}
                        checked={selectedPhilosophy === 'Existentialism'}
                        onChange={() => setSelectedPhilosophy('Existentialism')}
                    />
                    <span className={sharedClasses.text}>Existentialism</span>
                </label>
                <label className={sharedClasses.label}>
                    <input
                        type="radio"
                        name="philosophy"
                        className={sharedClasses.input}
                        checked={selectedPhilosophy === 'Eastern'}
                        onChange={() => setSelectedPhilosophy('Eastern')}
                    />
                    <span className={sharedClasses.text}>Eastern</span>
                </label>
                <button className={sharedClasses.button} onClick={handleSend}>Send</button>
            </div>
        </div>
    );
};

export default PhilosopherComponent;
