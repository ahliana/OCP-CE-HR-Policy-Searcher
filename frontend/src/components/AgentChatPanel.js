import React from 'react';
import Chatbot from './Chatbot';

function AgentChatPanel({
    wsRef,
    notice,
    onRunningChange,
}) {
    return (
        <div className="Agent-scanner" aria-label="Agent chat">
            <Chatbot
                wsRef={wsRef}
                notice={notice}
                onRunningChange={onRunningChange}
            />
        </div>
    );
}

export default AgentChatPanel;
