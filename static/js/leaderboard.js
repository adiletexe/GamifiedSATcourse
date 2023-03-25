const participants = [
  { name: 'Participant 1', value: 5, color: '#0F5298' },
  { name: 'Participant 2', value: 1, color: '#66D3FA' },
  { name: 'Participant 3', value: 15, color: '#D5F3FE' },
  { name: 'Participant 4', value: 12, color: '#2565AE' },
  { name: 'Participant 5', value: 3, color: '#FFA500' },
];

const raceProgressElement = document.querySelector('.race-progress');
const raceCars = document.querySelectorAll('.race-car');

let totalTime = 20;
let currentTime = 0;
let raceInterval = null;

function startRace() {
  // Reset race cars to starting positions
  raceCars.forEach(car => {
    car.classList.remove('race-car-progress');
    car.querySelector('.race-car-time').textContent = '0%';
  });

  // Start race interval
  raceInterval = setInterval(() => {
    // Update race progress
    currentTime++;
    const progressPercent = (currentTime / totalTime) * 100;

    // Update race car positions and times
    participants.forEach((participant, index) => {
      const carElement = document.getElementById(`car-${index + 1}`);
      const carTimeElement = carElement.querySelector('.race-car-time');

      if (participant.value / totalTime * 100 <= progressPercent) {
        carElement.classList.add('race-car-progress');
      } else {
        carElement.classList.remove('race-car-progress');
      }

      carTimeElement.textContent = `${Math.round(participant.value / totalTime * 100)}%`;
    });

    // End race if time is up
    if (currentTime >= totalTime) {
      clearInterval(raceInterval);
    }
  }, 100);
}

startRace();
