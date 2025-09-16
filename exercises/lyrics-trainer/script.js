let lyrics = [];
let currentLine = 0;
let isPlaying = false;
let playInterval = null;
let playbackDelay = 2000; // Default 2 seconds

async function loadLyrics() {
    try {
        const response = await fetch('lyrics.txt');
        const text = await response.text();
        lyrics = text.split('\n').filter(line => line.trim() !== '');

        if (lyrics.length > 0) {
            displayLine(0);
            updateButtons();
        } else {
            document.getElementById('current-line').textContent = 'No lyrics found';
        }
    } catch (error) {
        console.error('Error loading lyrics:', error);
        document.getElementById('current-line').textContent = 'Error loading lyrics';
    }
}

function displayLine(index) {
    if (index >= 0 && index < lyrics.length) {
        document.getElementById('current-line').textContent = lyrics[index];
        document.getElementById('line-number').textContent = index + 1;
        document.getElementById('line-counter').textContent = `Line ${index + 1} of ${lyrics.length}`;

        // Update progress bar
        const progress = ((index + 1) / lyrics.length) * 100;
        document.getElementById('progress-fill').style.width = `${progress}%`;

        currentLine = index;
    }
}

function nextLine() {
    if (currentLine < lyrics.length - 1) {
        displayLine(currentLine + 1);
    } else {
        displayLine(0); // Wrap around to beginning
    }
    updateButtons();
}

function prevLine() {
    if (currentLine > 0) {
        displayLine(currentLine - 1);
    } else {
        displayLine(lyrics.length - 1); // Wrap around to end
    }
    updateButtons();
}

function togglePlay() {
    if (isPlaying) {
        stopPlay();
    } else {
        startPlay();
    }
}

function startPlay() {
    isPlaying = true;
    document.getElementById('play-btn').textContent = 'Pause';
    document.getElementById('play-btn').classList.add('playing');

    playInterval = setInterval(() => {
        nextLine(); // Will automatically wrap around
    }, playbackDelay);
}

function stopPlay() {
    isPlaying = false;
    document.getElementById('play-btn').textContent = 'Play';
    document.getElementById('play-btn').classList.remove('playing');

    if (playInterval) {
        clearInterval(playInterval);
        playInterval = null;
    }
}

function updateButtons() {
    // Buttons are never disabled since we wrap around
    document.getElementById('prev-btn').disabled = false;
    document.getElementById('next-btn').disabled = false;
}

document.getElementById('next-btn').addEventListener('click', () => {
    if (isPlaying) stopPlay();
    nextLine();
});

document.getElementById('prev-btn').addEventListener('click', () => {
    if (isPlaying) stopPlay();
    prevLine();
});

document.getElementById('play-btn').addEventListener('click', togglePlay);

document.addEventListener('keydown', (e) => {
    switch(e.key) {
        case 'ArrowRight':
            if (!isPlaying) nextLine();
            break;
        case 'ArrowLeft':
            if (!isPlaying) prevLine();
            break;
        case ' ':
            e.preventDefault();
            togglePlay();
            break;
    }
});

// Speed slider event listener
document.getElementById('speed-slider').addEventListener('input', (e) => {
    playbackDelay = e.target.value * 1000; // Convert seconds to milliseconds
    document.getElementById('speed-value').textContent = `${e.target.value}s`;

    // If playing, restart with new speed
    if (isPlaying) {
        stopPlay();
        startPlay();
    }
});

loadLyrics();