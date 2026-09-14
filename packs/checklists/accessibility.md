# Accessibility checklist

For humans and agents before merging UI / docs / CLI help changes.

- [ ] Interactive controls have accessible names (visible label or `aria-label` / equivalent)
- [ ] Meaning is not conveyed by color alone
- [ ] New controls are reachable and operable by keyboard
- [ ] Focus order remains sensible after the change
- [ ] Meaningful images/icons have alt text or accessible names; decorative ones are marked decorative
- [ ] Dynamic status text uses existing live-region patterns (if any)—no spam
- [ ] Contrast remains readable for body text and primary controls (follow consumer tokens)
- [ ] Automated a11y lint/tests the repo already runs are green (do not invent new tooling mid-slice)
