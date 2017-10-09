# Background
- The idea here is to gather [Aubrey's answers to Quora questions](https://www.quora.com/profile/Aubrey-de-Grey) so that they can be searched more easily.
- Note that the goal is to *only* have those of his answers that are relevant to SENS. Aubrey also talks about mathematics on Quora, and that generally won't be of interest to us.
- Newer questions at the bottom.
  - It isn't clear to me whether it's better to have them at the bottom or the top.
- It would be nice to have a Python script that would scrape these automatically and store them at some easily-accessible URL...
- The script would ideally get not only the answers, but also Aubrey's responses to comments.

# Questions

##### How can I apply to SENS for funding?
2017.10.08 - http://www.sens.org/research/grant-submission-process

##### What is the significance of the failure of monoclonal antibodies that remove amyloid beta as an attempt to slow the progression of Alzheimer's disease to longevity research?
2017.09.25 - Less than most commentators say. Abeta may or may not be causative in AD, and if it is there are many ways in which it could be, but the important thing to remember is that AD is complicated, which means that the repair of more than one of its features may deliver more than the sum of the benefits arising from repairing each one in isolation. We have Abeta removal in our back pocket now as a tool that can be combined with other tools (such as tau removal) as and when the latter are developed. Whether it’s needed remains to be seen, but I’m very happy that we now have the option.

##### Why are billionaires that support the SENS agenda not really funding it?
2017.09.25 - Yeah… well, the thing about not funding someone is you don’t tend to be all that forthcoming about why you decided no… but my best inference is that there is no one answer, every HNWI is different. Sometimes they don’t think non-profits work. Sometimes they are scared that the approach is still unproven so they want to wait and see. Sometimes their spouse is virulently opposed. Sometimes they think other causes are more important. Sometimes they have a bad vibe about me personally. Sometimes they don’t like to do things that other HNWIs are not doing and they don’t consider Thiel to be a reliable first-mover. For each of the above reasons I could (but I won’t!) name at least one HNWI who I believe is substantially an example.

##### How much money does Aubrey de Grey need to find a cure?
2017.09.22 - Short answer: $1 billion over 10 years would do it with high probability.

Longer answer: clearly the question is not whether but when aging will be brought under comprehensive medical control. Thus, the right question is how much money is needed, over what time period, to hasten that time to the point where money will not make much difference any more because the rate of progress is limited by the simple difficulty of the research. See above for the number!

Key other number: at current funding levels we are going so slowly that (by my current estimate) we could easily end up delaying the defeat of aging by a decade. Therefore, even low-balling the expectations, every $2 spent in supporting this work would save a life. That compares very favourably with anything else.

##### What's been the progress, if any, on the WILT (Whole-body interdiction of the lengthening of telomeres) strategy?
2017.07.23 - It’s been slow but steady. On the telomere control side, other groups have made nice progress in inhibiting telomerase-mediated elongation (see especially Jerry Shay’s 2015 paper on 6-thio-2′-deoxyguanosine) and we have developed a much faster and cheaper assay for ALT that will facilitate the discovery of anti-ALT drugs. On the stem cell replacement side, we funded a study to look for the ability of early-generation telomerase-knockout haematopoietic stem cells to rescue longevity in late-generation telomerase knockout mice, and it worked (it was tricky because we needed to rescue their gut problems with another mutation) but we could only afford to do a small study so we barely made it to statistical significance and we haven’t published it. Our parallel work on the gut, led by Graca Almeida-Porada at Wake Forest, made modest progress but unfortunately we have had to suspend that project because of lack of funds.

I remain hopeful that we can get WILT to work - but I also remain hopeful that we won’t need to, because simpler therapies will work well enough. In particular, the progress in cancer immunotherapy over recent years has been dramatic, and it might just be enough to make WILT unnecessary. We won’t stop working on WILT until we’re sure that that is the case, though!

##### Do induced pluripotent stem cells reverse the intracellular junk that accumulates with aging?
2017.05.25 - Sure they do, but not because they are pluripotent: simply because the divide. Cell division shares out any junk between the daughter cells, so it dilutes it away.

##### Aubrey de Grey, what do you mean by "longevity escape velocity"?
2017.05.26 - The thing you’re overlooking is that the “first-generation” panel of rejuvenation therapies will not be perfect: it will mostly plug the gaps that evolution has left in our in-built damage-repair machinery, but it won’t do so 100%. (Let’s just define the damage that it does repair as the easy damage and the rest as the difficult damage.) There is nothing to stop us from applying those therapies every year, never mind every 30 years - but because of their incompleteness, however often we apply them we will still get back to biologically the same age (i.e., we’ll be carrying the same quantity of damage) at some point (I generally guess chronological age 90, but that’s a total guess) as we were just before we first applied the therapies. And the problem is, that the overwhelming majority of the damage that is present at that point will be difficult damage.

Thus, the only way we will be able to re-rejuvenate these people is if we have improved the therapies. And of course this carries on being true until such time as the therapies become truly 100% comprehensive, which quite probably will never happen. Hence the need to keep pushing ever closer towards that probably-unachievable goal. LEV is simple the minimum pace at which we need to do that, in order to keep one step ahead of the problem.

The good news is that LEV slows down as time passes, because the smaller the remaining gaps in the therapies, the longer it takes for that still-too-difficult damage to become abundant enough to make us sick.

##### Could CRISPR-modified CAR-T-cells clear senescent cells?
2017.03.27 - I’m guessing the question is stimulated by this recent study:

http://www.nature.com/nature/journal/v543/n7643/full/nature21405.html

Short answer: maybe, but it won’t be the end of the world if not, because there are now quite a few promising-looking ways to clear them. Our latest focus in this area is somewhat related: we’re starting to look at improving clearance with another arm of the immune system, NK cells, which are already known to clear most senescent cells following would healing so may be easiest to augment to do that job more thoroughly.

##### What does Aubrey de Grey think about the potential reversal of ageing in humans through Dr. Keizer's modified FOXO4-p53 interfering peptide?
2017.03.25 - The result is important, and the “DRI” technology used to do it is potentially even more important because it is so broadly applicable. We’ve known for a while that the elimination of senescent cells is a major plank of rejuvenation, and this is a further confirmation, with the advantage that it is underpinned by good scientific understanding of the mechanism.

##### What drugs can enhance the autophagy function of cells?
2017.03.14 - It’s important to remember that “autophagy” refers, strictly, to the processes that transport waste products to the lysosome, and not to the destruction of that waste once it gets there. This is not semantic hair-splitting, because it’s seductive but counterproductive to assume that enhancing autophagy will sustainably reduce the abundance of undigested waste in the rest of the cell. If there is too much such waste and the root cause of that is the lysosome’s inability to destroy it, no amount of enhancement of autophagy will help. And unfortunately, impairment (such as in aging) of lysosomal catabolic function seems to result, mainly, from the fact that that function is never 100% comprehensive even in youth, hence some types of waste accumulate there throughout life, with eventual upstream “traffic jam” consequences.

So there are plenty of answers to the question as asked, but really it’s the wrong question. The better question is, what drugs can sustainably enhance the lysosomal elimination of waste? And the answer to that, at present, is “none”. Enhancing that elimination requires enhancing the lysosome itself, which can only be done by giving it additional enzymes so that it can destroy stuff that it normally can’t. We’ve made good progress on that in a couple of key areas, atherosclerosis (oxidised cholesterol) and macular degeneration (derivatives of vitamin A), and both those programs have now been spun out into startups (Human Regenerative Biotechnologies and Ichor Therapeutics). We’ve recently started a new program in this area, targeting neurofibrillary tangles in Alzheimer’s.

##### Will Aubrey de Grey do a talk in France (or has he done one)?
I’ve given quite a few talks in France over the years. I haven’t honestly noticed a particularly greater susceptibility to this sort of thinking than elsewhere.

##### Which advice would Aubrey de Grey give to somebody with lupus erythematosus or arthritis as an autoimmune disease?
I’d advise consulting a medical professional, rather than anyone like myself whose doctorate is a PhD. We’re working on rejuvenating the immune system, which will certainly address autoimmunity to some extent as well as regular immune dysfunction, but our work on this, as on everything, is early-stage research and is years from being ready for prime time.

##### What does Aubrey de Grey think about the longevity pill Niagen?
Aubrey:
> Tim has it right.

Tim Amann:
> I obviously can’t speak for Aubrey de Grey, but I suspect he wouldn’t be interested in, or advocate for, Niagen. Niagen is a calorie restriction (CR) mimetic - a substance that supposedly mimics the effects of CR, which has been shown to have a significant longevity effect on short-lived organisms, but far less so on longer-lived organisms. Summing up the many things he has said about CR in the past, I would say he thinks CR would have little effect on human longevity. I wouldn’t say that he is against it. It’s just not his focus and not a game-changer in relation to aging.
> 
> In short, de Grey’s strategies are centered around removing and repairing the seven major forms of damage caused by aging (analogous to maintaining a classic car). He’s not attempting to stop or reverse the aging process (meaning he’s not trying to stop the damage from aging from occurring), which he would say is not doable for a very very long time due to the complexity of human metabolism.
> 
> CR mimetics are based on the idea of slowing the aging process (Niagen, Resveratrol, Metformin - pretty much any current “anti-aging pill”), but again, these will likely have little effect on longer-lived species like humans. Metformin will be going through a clinical trial, so we’ll know more soon, but I wouldn’t expect anything dramatic in relation to lifespan. I think de Grey estimated CR can provide, at the most, 2 to 3 more years in humans.
> 
> Niagen could potentially provide some benefits from a healthspan perspective (increased energy, potentially), but evidence is lacking. Time will tell.

##### Is it true that thanks to our technologies on aging, we have exceeded the limit of “in a lived year, we have gained more than a year to live”?
Definitely not. The rate at which the headline life expectancy numbers rise, which is a couple of months per year, does understate the situation for any given individual (basically because the headline numbers are statistical constructs generated from people born in different years), but it definitely doesn’t understate it enough to mean that we are already at “longevity escape velocity”. However, I remain of the view that we have at least a 50% chance of getting to that point within the next 20 years.

##### Is the first 5 year old mouse already alive (and is ongoing an anti-aging trial)?
Probably not - the current record of just one week shy of five years probably can’t be beaten by any practicable genetic manipulation. But what matters much more is what can be achieved using only interventions performed when the mouse is already alive, and ideally already middle-aged. At present the record for that is less than four years, so reaching five years is a very tall order - but I think there’s a good chance that the first such mouse will be born within five years.

##### Are there any good ways to invest in anti-aging research/therapies?
Wow… I’m not sure where to start with this one. The number of ways to invest in this space is exploding, and the most basic Google search will lead you to a host of opportunities. If you want more sophisticated advice on the best investment options. write to me at aubrey@sens.org and I’ll be happy to help.

##### How do T-lymphocytes have a lifespan that is infinite (according to my teacher)? Don't the telomeres get shorter until the cell dies?
T cells (and also B cells) turn on telomerase when they are in the highly proliferative phase, so they compensate for the telomere shortening that you’re thinking of. However, this telomerase activation weakens in old age, and that’s generally thought to be a big contributor to the age-related decline in the power of the immune system.

##### What's Aubrey de Grey's position on telomerase activators?
I’m very much on the fence. The question of whether telomerase activation will have decisive long-term negative consequences in terms of cancer is one that we cannot currently answer with confidence. Therefore, I very much endorse and support the research and clinical trials currently underway on telomerase activation, while at the same time SENS Research Foundation itself is heavily engaged in research to do the opposite, suppressing telomere elongation as an anti-cancer strategy.

##### Can we increase our maximum lifespan just by clearing senescent cells, beta amyloids, transthyretin and by immune system rejuvenation? Can we reach 150 years old?
What George said. The body accumulates many types of damage in the course of its normal operation, any of which will kill us on schedule unless it is eliminated (i.e., repaired) before it reaches fatal levels,however well we fix all the others. Fixing one major type of damage will **somewhat** slow down the accumultion of others, and I’ll admit that the magnitude of this interdependence may be a fair bit more than I would have thought before the results of the past few years in the senescent cell elimination area, but still, adding 70 years to today’s average lifespan of 80 is highly unlikely until we can rather thoroughly repair all seven of the main categories of damage.

##### What is your review of SENS Foundation?
Check out our annual report which should be released around the end of January.
