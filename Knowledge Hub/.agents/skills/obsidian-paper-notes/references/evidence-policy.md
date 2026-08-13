# Evidence Policy

Use evidence labels to prevent generated notes from overstating what is known.

## Claim Labels

| Label | Meaning | Safe phrasing |
| --- | --- | --- |
| `reported` | Claimed or reported by the paper or authors | `Paper báo cáo rằng...` |
| `observed` | Directly visible in a table, figure, equation, appendix, or protocol description | `Bảng 2 cho thấy...` |
| `inferred` | Analytical interpretation derived from the source | `Một cách diễn giải có thể là...` |
| `reproduced` | Obtained from an actual local experiment | `Kết quả tái lập local là...` |
| `unverified` | Plausible but not confirmed from a primary source or experiment | `Chưa xác minh...` |

Never present reported results as reproduced results.

## Personal Authorship

- Never write first-person personal reflections on behalf of the user.
- Preserve user-authored explanations, highlights, questions, ratings, and reading progress.
- Put generated explanations under `Diễn giải học tập`.
- Update `Ghi chú cá nhân` only when the user supplies the content or explicitly requests personal wording.
- Do not infer that the user has read or understood a paper because a generated note exists.

## Comparison Discipline

Before comparing empirical ML papers, record:

- dataset and split;
- evaluation scenario;
- backbone and trainable components;
- task order and task identity availability;
- memory or replay budget;
- shots/examples per class or relation;
- seeds, mean, standard deviation, or confidence intervals;
- metric definition and averaging;
- external data, retrieval corpus, generated data, or teacher model;
- compute and hardware;
- whether results are `reported`, `observed`, `inferred`, or `reproduced`.

Do not flatten incompatible protocols into one leaderboard.
