
const button = document.querySelector('#lotto-btn')
button.addEventListener('click', function() {
  // 컨테이너를 만들고
  const ballContainer = document.createElement('div')
  ballContainer.classList.add('ball-container')
  // 공을 만들어서 =>  6개를 만들어서
  const numbers = _.sampleSize(_.range(1, 46), 6)
  console.log(numbers)
  const ball = document.createElement('div')
  ball.classList.add('ball')
  ball.innerText = numbers[0]
  ball.style.backgroundColor = 'blue'
  // 컨테이너에 붙인다.
  ballContainer.appendChild(ball)
  // 컨테이너를 결과 영역에 붙인다. 
  const result = document.querySelector('#result')
  result.appendChild(ballContainer)
})

// 로또 공은 5가지 색깔로 되어 있습니다.
// 1번부터 10번까지는 노란색입니다.
// 11번 부터 20번까지는 파란색입니다.
// 21번부터 30번까지는 빨간색입니다.
// 31번부터 40번까지는 검은색입니다.
// 41번부터 45번까지는 초록색입니다.
