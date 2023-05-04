import { Auditory } from "./auditory.mjs";
import { Day } from "./day.mjs";
import { Lecture } from "./lecture.mjs";
import { Lecturer } from "./lecturer.mjs";
import { TimeSlot } from "./timeSlot.mjs";
import { TimeTable } from "./timetable.mjs";

const getRandomItem = <T extends any>(list: T[]): T => {
  return list[Math.floor(Math.random() * list.length)];
};

const auditoriesRaw = [
  {
    name: "235",
    capacity: 45,
  },
  {
    name: "304",
    capacity: 30,
  },
  {
    name: "306",
    capacity: 120,
  },
  {
    name: "705",
    capacity: 30,
  },
  {
    name: "1",
    capacity: 120,
  },
  {
    name: "232",
    capacity: 45,
  },
  {
    name: "212",
    capacity: 25,
  },
  {
    name: "317",
    capacity: 45,
  },
];

const daysRaw = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"];

const timeSlotsRaw = [
  "8:40 - 10.15",
  "10:35 - 12:10",
  "12:20 - 13:55",
  "14:05 - 15:40",
];

const lecturersRaw = [
  "Golubeva K.M.",
  "Marynych O.V.",
  "Chentsov O.I.",
  "Shishatska O.V.",
  "Cholyi V.Y.",
  "Livinska G.V.",
  "Karnaukh T.O.",
  "Panchenko T.V.",
  "Petrushchenkov S.P.",
  "Zavadsky I.O.",
  "Slabospytskyi O.S.",
  "Dolenko G.O.",
  "Veres M.M.",
  "Golubeva K.M.",
  "Kashpur O.F.",
  "Pichkur V.V.",
  "Mostovy V.S.",
  "Zavadsky I.O.",
  "Korobova M.V.",
  "Veres M.M.",
] as const;

const weeklyLecturesPlan = [
  {
    science: "Numerical methods",
    lecturer: "Golubeva K.M.",
    maxStudents: 100,
    type: "lecture",
    group: "MCC",
  },
  {
    science: "Computer networks",
    lecturer: "Golubeva K.M.",
    maxStudents: 35,
    type: "lab",
    group: "MCC",
  },
  {
    science: "Algebraic structures",
    lecturer: "Marynych O.V.",
    maxStudents: 35,
    type: "lab",
    group: "MCC",
  },
  {
    science: "Operational systems",
    lecturer: "Chentsov O.I.",
    maxStudents: 100,
    type: "lecture",
    group: "MCC",
  },
  {
    science: "Theory of programming",
    lecturer: "Shishatska O.V.",
    maxStudents: 35,
    type: "lab",
    group: "MCC",
  },
  {
    science: "Scientific image of the world",
    lecturer: "Cholyi V.Y.",
    maxStudents: 35,
    type: "lab",
    group: "MCC",
  },
  {
    science: "Probability theory",
    lecturer: "Livinska G.V.",
    maxStudents: 100,
    type: "lecture",
    group: "MCC",
  },
  {
    science: "Programming paradigms",
    lecturer: "Karnaukh T.O.",
    maxStudents: 100,
    type: "lecture",
    group: "MCC",
  },
  {
    science: "WEB technologies",
    lecturer: "Panchenko T.V.",
    maxStudents: 100,
    type: "lecture",
    group: "MCC",
  },
  {
    science: "Philosophy",
    lecturer: "Petrushchenkov S.P.",
    maxStudents: 100,
    type: "lecture",
    group: "MCC",
  },
  {
    science: "Theory of quantum computing",
    lecturer: "Zavadsky I.O.",
    maxStudents: 35,
    type: "lab",
    group: "MCC",
  },
  {
    science: "Data Analysis",
    lecturer: "Slabospytskyi O.S.",
    maxStudents: 100,
    type: "lecture",
    group: "DO",
  },
  {
    science: "System optimization",
    lecturer: "Dolenko G.O.",
    maxStudents: 35,
    type: "lecture",
    group: "DO",
  },
  {
    science: "Theory of functions of a complex variable",
    lecturer: "Veres M.M.",
    maxStudents: 35,
    type: "lab",
    group: "DO",
  },
  {
    science: "Basics of calculation methods",
    lecturer: "Golubeva K.M.",
    maxStudents: 35,
    type: "lab",
    group: "DO",
  },
  {
    science: "Equations of mathematical physics",
    lecturer: "Pichkur V.V.",
    maxStudents: 35,
    type: "lab",
    group: "DO",
  },
  {
    science: "Management theory",
    lecturer: "Pichkur V.V.",
    maxStudents: 35,
    type: "lecture",
    group: "DO",
  },
  {
    science: "AI models and algorithms",
    lecturer: "Mostovy V.S.",
    maxStudents: 35,
    type: "lab",
    group: "DO",
  },
  {
    science: "Databases and information systems",
    lecturer: "Zavadsky I.O.",
    maxStudents: 35,
    type: "lecture",
    group: "DO",
  },
  {
    science: "Ecological and economic processes",
    lecturer: "Korobova M.V.",
    maxStudents: 35,
    type: "lab",
    group: "DO",
  },
  {
    science: "Ruby programming",
    lecturer: "Veres M.M.",
    maxStudents: 35,
    type: "lab",
    group: "DO",
  },
] satisfies {
  science: string;
  group: string;
  type: "lecture" | "lab";
  lecturer: string;
  maxStudents: number;
}[];

const timings = timeSlotsRaw.map((e) => new TimeSlot(e));
const days = daysRaw.map((e) => new Day(e));
const auditories = auditoriesRaw.map((e) => new Auditory(e.name, e.capacity));
const lecturers = lecturersRaw.map((e) => new Lecturer(e));

export const makeInitialPopulation = (count = 20) => {
  return [...new Array(count)].map(() => {
    const lections = weeklyLecturesPlan.map((e) => {
      const lecturer = lecturers.filter((l) => l.name === e.lecturer).at(0);
      if (!lecturer) {
        throw new Error(`unknown lecturer in ${JSON.stringify(e, null, 2)}`);
      }
      return initializeLection({
        ...e,
        lecturer,
      });
    });
    return new TimeTable(lections);
  });
};

const initializeLection = (e: {
  science: string;
  group: string;
  type: "lecture" | "lab";
  lecturer: Lecturer;
  maxStudents: number;
}) =>
  new Lecture(
    e.science,
    getRandomItem(timings),
    getRandomItem(auditories),
    getRandomItem(lecturers),
    e.type,
    e.group,
    getRandomItem(days),
    e.maxStudents
  );
