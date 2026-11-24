"""Framing text for GxP. Everything else is read from the design."""

DESIGN = 'CSW-GxP-Reference-Design.md'

TREE = {'kicker': 'GxP',
 'rail': ['Label queries keep scope membership current automatically',
          'Every in-scope workload resolves into exactly one scope',
          'The tree is the boundary an assessor will ask you to defend'],
 'sub': 'The scope hierarchy this design recommends, with label-driven membership so the '
        'boundary stays current as the estate changes.',
 'takeaway': 'Scope membership is <b>label-driven, not a static list</b>, so the boundary '
             'stays accurate as the estate changes. Scope accuracy is itself evidence in most '
             'assessments.',
 'takeaway_tag': 'Key Takeaway',
 'title': 'Scope Architecture',
 'title_tail': '&mdash; GxP'}

WORKFLOW = None

PHASES = {'card_h': 232,
 'caution': 'CSW supplies evidence for computerised-system controls and segmentation. '
            'Validation of the GxP system itself stays with the quality organisation.',
 'caution_label': 'Evidence boundary &rsaquo;',
 'kicker': 'EU GMP ANNEX 11 &middot; 21 CFR PART 11',
 'rail': ['Build the QA gate into the project plan from day one',
          'Simulate first &mdash; the output is what QA approves',
          'Compensating controls carry the un-patchable systems'],
 'sub': 'The phase plan this design follows, from sensor coverage through ongoing compliance '
        'posture. Each phase heading and its work items come from the design itself.',
 'takeaway': 'Each enforcement step is a change to a validated environment and needs its own '
             'change-control record. <b>Simulation output is the evidence package that gets '
             'the change approved</b> &mdash; which makes simulate-before-enforce a regulatory '
             'feature here, not just a safety feature.',
 'takeaway_tag': 'Key Takeaway',
 'title': 'GxP deployment',
 'title_tail': ' &mdash; seven phases',
 'width': 1900}
