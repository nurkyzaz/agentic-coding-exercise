export const BlockExercise = async () => ({
  "tool.execute.before": async (input, output) => {
    if (JSON.stringify(output.args).includes("EXERCISE.md"))
      throw new Error("EXERCISE.md is the participant brief and is off-limits to the agent. Ask the user for instructions instead.")
  },
})
