import type { Auditory } from "./auditory.mjs";
import type { Day } from "./day.mjs";
import type { Lecturer } from "./lecturer.mjs";
import type { TimeSlot } from "./timeSlot.mjs";

export class Lecture {
  constructor(
    public readonly science: string,
    public readonly timing: TimeSlot,
    public readonly auditory: Auditory,
    public readonly lecturer: Lecturer,
    public readonly type: "lecture" | "lab",
    public readonly group: string,
    public readonly day: Day,
    public readonly maxStudents: number
  ) {}

  auditoryMismatch(): number {
    return this.maxStudents > this.auditory.capacity ? 1 : 0;
  }

  conflicts(p: Lecture): number {
    if (!(p.day === this.day && p.timing === this.timing)) {
      return 0;
    }
    let conflicts = 0;
    // auditory conflict
    if (
      this.auditory === p.auditory &&
      (p.group !== this.group ||
        p.lecturer !== this.lecturer ||
        p.science !== this.science ||
        p.type !== this.type)
    ) {
      conflicts += 1;
    }
    // group conflict
    if (
      this.group === p.group &&
      (this.auditory !== p.auditory ||
        p.lecturer !== this.lecturer ||
        p.science !== this.science ||
        p.type !== this.type)
    ) {
      conflicts += 1;
    }
    // lecturer conflict
    if (
      this.lecturer === p.lecturer &&
      (this.auditory !== p.auditory ||
        p.group !== this.group ||
        p.science !== this.science ||
        p.type !== this.type)
    ) {
      conflicts += 1;
    }
    return conflicts;
  }
}
