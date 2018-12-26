const MAX_CIVS = 3;

selectCiv = () => {
  const allCivs = document.getElementsByClassName("civ");
  // console.log(allCivs);

  let checkedCivs = [];
  for (let civ of allCivs) {
    if (civ.checked) {
      checkedCivs.push(civ);
    }
  }

  let civIndicies = randomCivs(checkedCivs.length);

  document.getElementById("result-civ-1").innerHTML =
    "1. " + checkedCivs[civIndicies[0]].value;
  document.getElementById("result-civ-2").innerHTML =
    "2. " + checkedCivs[civIndicies[1]].value;
  document.getElementById("result-civ-3").innerHTML =
    "3. " + checkedCivs[civIndicies[2]].value;
};

randomCivs = max => {
  let indicies = [];
  for (let i = 0; i < max; i++) {
    indicies.push(i);
  }

  let randomResult = [];
  for (let i = 0; i < MAX_CIVS; i++) {
    let randomIndex = randomInt(indicies.length);
    while (randomResult.includes(randomIndex)) {
      randomIndex = randomInt(indicies.length);
    }
    randomResult.push(randomIndex);
  }

  return randomResult;
};

randomInt = max => {
  return Math.floor(Math.random() * max);
};
