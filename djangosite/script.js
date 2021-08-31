import delay from './delay';
import people from './people';

const add = async function (a, b) {
  delay(10);
  //if (a < 0) throw new Error ("Not supported")

  return a + b;
};

const result = await add(-2, 3);
result = 1;
people.map((p) => p.age);
